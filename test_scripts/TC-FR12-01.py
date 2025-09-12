Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-12: Contentful CMS Integration', () => {
    before(async () => { await browser.url('https://app.contentful.com'); });
    it('Positive - Verify that Contentful integration is functioning correctly for modular content', async () => {
        const interface = await $('.contentful-interface');
        await expect(interface).toBeDisplayed();
        const contentInput = await $('.content-input');
        await contentInput.setValue('New Content');
        const publish = await $('.publish');
        await publish.click();
        await browser.url('http://www.ipsy.com');
        const displayedContent = await $('.displayed-content');
        await expect(displayedContent).toHaveText('New Content');
    });
    it('Negative - Verify failure if content not published', async () => {
        const contentInput = await $('.content-input');
        await contentInput.setValue('Unpublished');
        await browser.url('http://www.ipsy.com');
        const displayedContent = await $('.displayed-content');
        await expect(displayedContent).not.toHaveText('Unpublished');
    });
    it('Edge - Verify with large content payload', async () => {
        const contentInput = await $('.content-input');
        await contentInput.setValue('A'.repeat(10000));
        const publish = await $('.publish');
        await publish.click();
        await browser.url('http://www.ipsy.com');
        const displayedContent = await $('.displayed-content');
        await expect(displayedContent).toBeDisplayed();
    });
});
