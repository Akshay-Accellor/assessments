Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-13: Xenia Integration with Contentful', () => {
    before(async () => { await browser.url('https://app.contentful.com/settings'); });
    it('Positive - Verify integration with Xenia for A/B testing', async () => {
        const xeniaSettings = await $('.xenia-settings');
        await expect(xeniaSettings).toBeDisplayed();
        const linkButton = await $('.link-xenia');
        await linkButton.click();
        const testCreate = await $('.create-ab-test');
        await testCreate.click();
        const noError = await $('.no-error');
        await expect(noError).toBeDisplayed();
    });
    it('Negative - Verify integration fails with invalid credentials', async () => {
        const linkButton = await $('.link-xenia');
        await linkButton.click();
        const errorMessage = await $('.error-message');
        await expect(errorMessage).toBeDisplayed();
    });
    it('Edge - Verify multiple A/B tests creation', async () => {
        const testCreate = await $('.create-ab-test');
        await testCreate.click();
        await testCreate.click();
        const noError = await $('.no-error');
        await expect(noError).toBeDisplayed();
    });
});
